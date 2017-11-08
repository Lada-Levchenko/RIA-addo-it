from peewee import *
from utils.codes import *


database = PostgresqlDatabase('ria', **{'user': 'postgres'})
# database = SqliteDatabase('ria')


def init_db():
    database.create_tables([IAPDReport, Indvl, CrntEmp, PrevRgstn, BrnchOfLoc, CrntRgstn,
                           DRP, Dsgntn, EmpHist, Exm, Info, OthrBus, OthrNm, PrevBrnchOfLoc], safe=True)


answer_yes_no = {
    ("Y", "Y"),
    ("N", "N")
}


class BaseModel(Model):
    class Meta:
        database = database


class IAPDReport(BaseModel):
    gen_on = DateTimeField()

    class Meta:
        db_table = 'iapdreport'


class Indvl(BaseModel):
    iapd_report = ForeignKeyField(IAPDReport, related_name='indvls')

    class Meta:
        db_table = 'indvl'


class CrntEmp(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='crnt_emps')
    org_nm = CharField(null=True, max_length=64)    # shouldn't be null!!
    org_pk = IntegerField(null=True)    # shouldn't be null!!
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'crntemp'


class PrevRgstn(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='prev_rgstns', null=True)
    org_nm = CharField(null=True, max_length=64)    # shouldn't be null!!
    org_pk = IntegerField(null=True)    # shouldn't be null!!
    reg_begin_dt = DateTimeField(null=True)
    reg_end_dt = DateTimeField(null=True)

    class Meta:
        db_table = 'prevrgstn'


class BrnchOfLoc(BaseModel):
    crnt_emp = ForeignKeyField(CrntEmp, related_name='brnch_of_locs', null=True)
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'brnchofloc'


class PrevBrnchOfLoc(BaseModel):
    prev_rgstn = ForeignKeyField(PrevRgstn, related_name='prev_brnch_of_locs', null=True)
    city = CharField(null=True, max_length=50)
    state = CharField(null=True, choices=state_code)

    class Meta:
        db_table = 'prevbrnchofloc'


class CrntRgstn(BaseModel):
    crnt_emp = ForeignKeyField(CrntEmp, related_name='crnt_rgstns')
    reg_auth = CharField(null=True, choices=state_code)    # shouldn't be null!!
    reg_cat = CharField(null=True, choices=registration_category)    # shouldn't be null!!
    st = CharField(null=True, choices=registration_status)    # shouldn't be null!!
    st_dt = DateTimeField(null=True)    # shouldn't be null!!

    class Meta:
        db_table = 'crntrgstn'


class DRP(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='drps')
    has_reg_action = CharField(null=True, choices=answer_yes_no)
    has_criminal = CharField(null=True, choices=answer_yes_no)
    has_bankrupt = CharField(null=True, choices=answer_yes_no)
    has_civil_judc = CharField(null=True, choices=answer_yes_no)
    has_bond = CharField(null=True, choices=answer_yes_no)
    has_judgment = CharField(null=True, choices=answer_yes_no)
    has_invstgn = CharField(null=True, choices=answer_yes_no)
    has_cust_comp = CharField(null=True, choices=answer_yes_no)
    has_termination = CharField(null=True, choices=answer_yes_no)

    class Meta:
        db_table = 'drp'


class Dsgntn(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='dsgntns')
    dsgntn_nm = CharField(null=True, max_length=128)    # shouldn't be null!!

    class Meta:
        db_table = 'dsgntn'


class EmpHist(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='emp_hss')
    from_dt = CharField(null=True, max_length=7)    # shouldn't be null!!
    to_dt = CharField(null=True, max_length=7)    # shouldn't be null!!
    org_nm = CharField(null=True, max_length=64)    # shouldn't be null!!
    city = CharField(null=True, max_length=50)    # shouldn't be null!!
    state = CharField(null=True, choices=state_code)

    class Meta:
        db_table = 'emphist'


class Exm(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='exms')
    exm_cd = CharField(null=True, choices=exam_code)    # shouldn't be null!!
    exm_dt = DateTimeField(null=True)
    exm_nm = CharField(null=True, max_length=128)    # shouldn't be null!!

    class Meta:
        db_table = 'exm'


class Info(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='info')
    actv_ag_reg = CharField(null=True, choices=answer_yes_no)
    indvl_pk = IntegerField()
    link = CharField(null=True, max_length=128)
    first_nm = CharField(null=True, max_length=25)
    last_nm = CharField(null=True, max_length=25)
    mid_nm = CharField(null=True, max_length=20)
    suf_nm = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'info'


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
