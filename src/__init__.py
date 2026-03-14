"""
File Organizer Automation Package
"""

from src.file_organizer import FileOrganizer
from src.file_types import get_category, FILE_TYPES
from src.logger import setup_logger

__version__ = '1.0.0'
__author__ = 'Soundariya2006'

__all__ = ['FileOrganizer', 'get_category', 'FILE_TYPES', 'setup_logger']