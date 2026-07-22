from rest_framework.exceptions import APIException
from rest_framework import status

class BaseException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Erro na solicitacao'
    default_code = 'error'

class ValidationError(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Dados invalidos'
    default_code = 'validation_error'

class PermissionDenied(BaseException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Voce nao tem permissao para acessar este recurso'
    default_code = 'permission_denied'

class ResourceNotFound(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Recurso nao encontrado'
    default_code = 'not_found'

class ConflictError(BaseException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Conflito ao processar a solicitacao'
    default_code = 'conflict'

class AuthenticationFailed(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Falha na autenticacao'
    default_code = 'authentication_failed'

class InvalidCredentials(AuthenticationFailed):
    default_detail = 'Usuario ou senha invalidos'
    default_code = 'invalid_credentials'

class AccountLocked(AuthenticationFailed):
    default_detail = 'Conta bloqueada por multiplas tentativas falhadas'
    default_code = 'account_locked'
