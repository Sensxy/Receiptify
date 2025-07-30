import os
import shutil
from typing import Optional
from fastapi import UploadFile
import uuid
from datetime import datetime

class StorageService:
    """
    Storage service that can easily switch between local and S3 storage.
    Just change the implementation later without changing the interface.
    """
    
    def __init__(self, storage_type: str = "local"):
        self.storage_type = storage_type
        self.local_upload_dir = "uploads"
        
        # Create uploads directory if it doesn't exist
        if not os.path.exists(self.local_upload_dir):
            os.makedirs(self.local_upload_dir)
    
    async def save_file(self, file: UploadFile, user_id: int) -> str:
        """
        Save uploaded file and return the file URL/path.
        This interface works for both local and S3 storage.
        """
        if self.storage_type == "local":
            return await self._save_local(file, user_id)
        elif self.storage_type == "s3":
            return await self._save_s3(file, user_id)
        else:
            raise ValueError(f"Unsupported storage type: {self.storage_type}")
    
    async def _save_local(self, file: UploadFile, user_id: int) -> str:
        """Save file locally for development"""
        # Generate unique filename
        file_extension = file.filename.split('.')[-1] if '.' in file.filename else 'jpg'
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        
        # Create user-specific folder
        user_folder = os.path.join(self.local_upload_dir, f"user_{user_id}")
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
        
        # Full file path
        file_path = os.path.join(user_folder, unique_filename)
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Return relative path that can be served by FastAPI
        return f"/uploads/user_{user_id}/{unique_filename}"
    
    async def _save_s3(self, file: UploadFile, user_id: int) -> str:
        """
        Save file to AWS S3 (implement later)
        This is where you'd use boto3 to upload to S3
        """
        # TODO: Implement S3 upload
        # import boto3
        # s3_client = boto3.client('s3')
        # s3_client.upload_fileobj(file.file, bucket_name, key)
        # return f"https://{bucket_name}.s3.amazonaws.com/{key}"
        pass
    
    def get_file_url(self, file_path: str) -> str:
        """Convert internal file path to public URL"""
        if self.storage_type == "local":
            return f"http://localhost:8000{file_path}"
        elif self.storage_type == "s3":
            return file_path  # S3 URLs are already complete
        
    def delete_file(self, file_path: str) -> bool:
        """Delete file from storage"""
        if self.storage_type == "local":
            try:
                # Convert URL back to local path
                local_path = file_path.replace("/uploads/", "uploads/")
                if os.path.exists(local_path):
                    os.remove(local_path)
                    return True
            except Exception:
                pass
        return False

# Create global storage service instance
storage_service = StorageService(storage_type="local")