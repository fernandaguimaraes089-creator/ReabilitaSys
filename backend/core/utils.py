import uuid
from datetime import datetime
from django.utils import timezone

def generate_unique_id(prefix=''):
    """Gera ID unico com prefixo opcional"""
    return f"{prefix}{uuid.uuid4().hex[:8].upper()}"

def get_current_date():
    """Retorna data atual no timezone da aplicacao"""
    return timezone.now().date()

def get_current_datetime():
    """Retorna data/hora atual no timezone da aplicacao"""
    return timezone.now()

def calculate_age(birth_date):
    """Calcula idade baseado na data de nascimento"""
    today = get_current_date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def format_phone(phone):
    """Formata numero de telefone"""
    phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    if len(phone) == 11:
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
    elif len(phone) == 10:
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"
    return phone

def format_cpf(cpf):
    """Formata CPF"""
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf

def format_rg(rg):
    """Formata RG"""
    rg = rg.replace('.', '').replace('-', '')
    if len(rg) >= 8:
        return f"{rg[0:1]}.{rg[1:4]}.{rg[4:7]}-{rg[7:8]}"
    return rg
