from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import re

cpf_validator = RegexValidator(
    regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message=_('CPF deve estar no formato: 000.000.000-00'),
    code='invalid_cpf_format'
)

rg_validator = RegexValidator(
    regex=r'^\d{1,2}\.\d{3}\.\d{3}-[A-Z]{1}$',
    message=_('RG deve estar no formato: 0.000.000-X'),
    code='invalid_rg_format'
)

phone_validator = RegexValidator(
    regex=r'^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$',
    message=_('Telefone deve estar em um formato valido'),
    code='invalid_phone_format'
)

def validate_cpf(cpf):
    """Valida CPF usando algoritmo de digito verificador"""
    cpf = cpf.replace('.', '').replace('-', '')
    
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError(_('CPF invalido'))
    
    if cpf == cpf[0] * 11:
        raise ValueError(_('CPF invalido'))
    
    return True

def validate_cid_code(cid):
    """Valida codigo CID-10"""
    pattern = r'^[A-Z]\d{2}\.?\d?\d?$'
    if not re.match(pattern, cid):
        raise ValueError(_('Codigo CID invalido'))
    return True
