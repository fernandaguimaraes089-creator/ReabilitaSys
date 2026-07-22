from rest_framework import viewsets

class AuditMixin:
    """Mixin para auditoria automatica"""
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    
    def perform_destroy(self, instance):
        instance.soft_delete(self.request.user)

class TimestampMixin:
    """Mixin para adicionar timestamps ao serializer"""
    
    def get_fields(self):
        fields = super().get_fields()
        if 'created_at' in fields:
            fields['created_at'].read_only = True
        if 'updated_at' in fields:
            fields['updated_at'].read_only = True
        return fields

class SoftDeleteMixin(viewsets.ModelViewSet):
    """Mixin para soft delete automatico"""
    
    def get_queryset(self):
        queryset = super().get_queryset()
        include_deleted = self.request.query_params.get('include_deleted', 'false').lower() == 'true'
        
        if include_deleted:
            return queryset.all_with_deleted()
        return queryset
    
    def perform_destroy(self, instance):
        instance.soft_delete(self.request.user)
