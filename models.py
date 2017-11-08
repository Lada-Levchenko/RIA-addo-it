from peewee import *
from utils.codes import *


database = PostgresqlDatabase('ria', **{'user': 'postgres'})
# database = SqliteDatabase('ria')


def init_db():
    database.create_tables([IAPDIndividualReport, Individual, CurrentEmployment, PreviousRegistration,
                            BranchOfficeLocation, CurrentRegistration, DRP, Designation, EmploymentHistory,
                            Exam, Info, OtherBusiness, OtherName, PreviousBranchOfficeLocation], safe=True)


answer_yes_no = {
    ("Y", "Y"),
    ("N", "N")
}


class BaseModel(Model):
    class Meta:
        database = database


class IAPDIndividualReport(BaseModel):
    gen_on = DateTimeField()

    class Meta:
        db_table = 'iapd_individual_report'


class Individual(BaseModel):
    iapd_report = ForeignKeyField(IAPDIndividualReport, related_name='indvls')

    class Meta:
        db_table = 'individual'


class CurrentEmployment(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='crnt_emps')
    org_nm = CharField(null=True, max_length=64)    # shouldn't be null!!
    org_pk = IntegerField(null=True)    # shouldn't be null!!
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'current_employment'


class PreviousRegistration(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='prev_rgstns', null=True)
    org_nm = CharField(null=True, max_length=64)    # shouldn't be null!!
    org_pk = IntegerField(null=True)    # shouldn't be null!!
    reg_begin_dt = DateTimeField(null=True)
    reg_end_dt = DateTimeField(null=True)

    class Meta:
        db_table = 'previous_registration'


class BranchOfficeLocation(BaseModel):
    crnt_emp = ForeignKeyField(CurrentEmployment, related_name='brnch_of_locs', null=True)
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'branch_office_location'


class PreviousBranchOfficeLocation(BaseModel):
    prev_rgstn = ForeignKeyField(PreviousRegistration, related_name='prev_brnch_of_locs', null=True)
    city = CharField(null=True, max_length=50)
    state = CharField(null=True, choices=state_code)

    class Meta:
        db_table = 'previous_branch_office_location'


class CurrentRegistration(BaseModel):
    crnt_emp = ForeignKeyField(CurrentEmployment, related_name='crnt_rgstns')
    reg_auth = CharField(null=True, choices=state_code)    # shouldn't be null!!
    reg_cat = CharField(null=True, choices=registration_category)    # shouldn't be null!!
    st = CharField(null=True, choices=registration_status)    # shouldn't be null!!
    st_dt = DateTimeField(null=True)    # shouldn't be null!!

    class Meta:
        db_table = 'current_registration'


class DRP(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='drps')
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


class Designation(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='dsgntns')
    dsgntn_nm = CharField(null=True, max_length=128)    # shouldn't be null!!

    class Meta:
        db_table = 'designation'


class EmploymentHistory(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='emp_hss')
    from_dt = CharField(null=True, max_length=7)    # shouldn't be null!!
    to_dt = CharField(null=True, max_length=7)    # shouldn't be null!!
    org_nm = CharField(null=True, max_length=64)    # shouldn't be null!!
    city = CharField(null=True, max_length=50)    # shouldn't be null!!
    state = CharField(null=True, choices=state_code)

    class Meta:
        db_table = 'employment_history'


class Exam(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='exms')
    exm_cd = CharField(null=True, choices=exam_code)    # shouldn't be null!!
    exm_dt = DateTimeField(null=True)
    exm_nm = CharField(null=True, max_length=128)    # shouldn't be null!!

    class Meta:
        db_table = 'exam'


class Info(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='info')
    actv_ag_reg = CharField(null=True, choices=answer_yes_no)
    indvl_pk = IntegerField()
    link = CharField(null=True, max_length=128)
    first_nm = CharField(null=True, max_length=25)
    last_nm = CharField(null=True, max_length=25)
    mid_nm = CharField(null=True, max_length=20)
    suf_nm = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'info'


class OtherBusiness(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='othr_buss')
    desc = CharField(max_length=4000)

    class Meta:
        db_table = 'other_business'


class OtherName(BaseModel):
    indvl = ForeignKeyField(Individual, related_name='othr_nms')
    first_nm = CharField(null=True, max_length=25)
    last_nm = CharField(null=True, max_length=25)
    mid_nm = CharField(null=True, max_length=20)
    suf_nm = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'other_name'
