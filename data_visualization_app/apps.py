"""
This module contains the configuration for the Django application.
"""
from django.apps import AppConfig


class DataVisualizationConfig(AppConfig):
    """Configuration for the Data Visualization app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_visualization'
