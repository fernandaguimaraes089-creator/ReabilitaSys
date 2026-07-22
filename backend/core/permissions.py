from rest_framework import permissions

class IsAdministrator(permissions.BasePermission):
    """Apenas administradores"""
    message = 'Apenas administradores podem acessar este recurso.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)

class IsCoordination(permissions.BasePermission):
    """Apenas coordenacao"""
    message = 'Apenas coordenacao pode acessar este recurso.'
    
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'coordination'
        )

class IsReception(permissions.BasePermission):
    """Apenas recepcao"""
    message = 'Apenas recepcao pode acessar este recurso.'
    
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'reception'
        )

class IsNursing(permissions.BasePermission):
    """Apenas enfermagem"""
    message = 'Apenas enfermagem pode acessar este recurso.'
    
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'nursing'
        )

class IsFinancial(permissions.BasePermission):
    """Apenas financeiro"""
    message = 'Apenas financeiro pode acessar este recurso.'
    
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'financial'
        )

class IsReadOnly(permissions.BasePermission):
    """Permissao apenas leitura"""
    
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
