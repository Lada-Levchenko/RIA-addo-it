from peewee import *
from utils.codes import *

database = PostgresqlDatabase('ria', **{'user': 'postgres'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class IAPDReport(BaseModel):
    gen_on = DateTimeField()
    # indvl = ForeignKeyField()

    class Meta:
        db_table = 'iapdreport'


class Indvl(BaseModel):
    iapd_report = ForeignKeyField(IAPDReport, related_name='indvls')

    class Meta:
        db_table = 'indvl'


class CrntEmp(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='crnt_emps')
    org_nm = CharField(max_length=64)
    org_pk = IntegerField()       # Int10!!
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'crntemp'


class BrnchOfLoc(BaseModel):
    crnt_emp = ForeignKeyField(CrntEmp, related_name='brnch_of_locs')
    prev_rgstns = ForeignKeyField(PrevRgstn, related_name='brnch_of_locs')
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'brnchofloc'


# complete
class CrntRgstn(BaseModel):
    crnt_emp = ForeignKeyField(CrntEmp, related_name='crnt_rgstns')
    reg_auth = CharField(choices=state_code)
    reg_cat = CharField(choices=registration_category)
    st = CharField(choices=registration_status)
    st_dt = DateTimeField()

    class Meta:
        db_table = 'crntrgstn'


# complete
class DRP(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='drps')
    has_reg_action = BooleanField(null=True)
    has_criminal = BooleanField(null=True)
    has_bankrupt = BooleanField(null=True)
    has_civil_judc = BooleanField(null=True)
    has_bond = BooleanField(null=True)
    has_judgment = BooleanField(null=True)
    has_invstgn = BooleanField(null=True)
    has_cust_comp = BooleanField(null=True)
    has_termination = BooleanField(null=True)

    class Meta:
        db_table = 'drp'


# complete
class Dsgntn(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='dsgntns')
    dsgntn_nm = CharField(max_length=128)

    class Meta:
        db_table = 'dsgntn'


class EmpHist(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='emp_hss')
    from_dt = CharField(max_length=7)
    to_dt = CharField(max_length=7)
    org_nm = CharField(max_length=64)
    city = CharField(max_length=50)
    state = CharField(null=True, choices=state_code)

    class Meta:
        db_table = 'emphist'


class Exm(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='exms')
    exm_cd = CharField(choices=exam_code)
    exm_dt = DateTimeField(null=True)
    exm_nm = CharField(max_length=128)

    class Meta:
        db_table = 'exm'


class Info(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='info')
    actv_ag_reg = BooleanField()
    indvlp_k = IntegerField()       # Int10!!
    link = CharField(null=True, max_length=128)
    first_nm = CharField(null=True, max_length=25)
    last_nm = CharField(null=True, max_length=25)
    mid_nm = CharField(null=True, max_length=20)
    suf_nm = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'info'


# complete
class OthrBus(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='othr_buss')
    desc = CharField(max_length=4000)

    class Meta:
        db_table = 'othrbus'


class OthrNm(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='othr_nms')
    first_nm = CharField(null=True, max_length=25)
    last_nm = CharField(null=True, max_length=25)
    mid_nm = CharField(null=True, max_length=20)
    suf_nm = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'othrnm'


class PrevRgstn(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='prev_rgstns')
    iapd_report = ForeignKeyField(IAPDReport, related_name='prev_rgstns')
    org_nm = CharField(max_length=64)
    org_pk = IntegerField()       # Int10!!
    reg_begin_dt = DateTimeField(null=True)
    reg_end_dt = DateTimeField(null=True)

    class Meta:
        db_table = 'prevrgstn'
