from django.db import models


class JobTaskDefault(models.Model):
    """
        This model holds the DEFAULT job tasks associated with a SWMS Group. These should NOT be editable.
    """
    RISK_LEVEL = (
        ('1L', '1L'),
        ('2M', '2M'),
        ('3H', '3H'),
        ('4A', '4A'),
    )
    name = models.CharField(max_length=400, null=True)
    hazards = models.CharField(max_length=400, null=True)
    hazard_risk = models.CharField(max_length=100, null=True, choices=RISK_LEVEL)
    control_measures = models.CharField(max_length=400, null=True)
    control_risk = models.CharField(max_length=100, null=True, choices=RISK_LEVEL)
    responsible_person = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class SwmsGroupDefault(models.Model):
    """
            This model holds the DEFAULT SWMS Groups. These should NOT be editable.
    """
    name = models.CharField(max_length=100, null=True, unique=True)
    job_task = models.ManyToManyField(JobTaskDefault)

    def __str__(self):
        return self.name


class Swms(models.Model):

    # site details
    site_name = models.CharField(max_length=100, null=True)
    site_number = models.CharField(max_length=100, null=True)
    site_contact = models.CharField(max_length=100, null=True)
    site_email = models.CharField(max_length=100, null=True)

    # job details
    JOB_TYPE = (
        ('MW', 'MW'),
        ('C', 'C'),
        ('M', 'M'),
        ('S', 'S')
    )

    job_type = models.CharField(max_length=100, null=True, choices=JOB_TYPE)
    job_number = models.CharField(max_length=100, null=True)

    # extreme fire details
    efs_name = models.CharField(max_length=100, null=True)
    efs_manager_name = models.CharField(max_length=100, null=True)
    efs_manager_email = models.CharField(max_length=100, null=True)
    efs_phone_number = models.CharField(max_length=100, null=True)
    efs_signature = models.CharField(max_length=100, null=True) #signed on ipad
    swms_groups = models.CharField(max_length=100, null=True, blank=True)

    # general details
    date_created = models.DateTimeField(auto_now_add=True)

    # hazardous & environmental impacts
    electrical_equipment = models.BooleanField()
    hot_work = models.BooleanField()
    noise_vibration = models.BooleanField()
    fuels_oils_chemicals = models.BooleanField()
    elevated_levels = models.BooleanField()
    hazardous_manual_tasks = models.BooleanField()
    native_vegetation_weeds = models.BooleanField()
    terrestrial_fauna = models.BooleanField()
    slips_trips_falls = models.BooleanField()
    outdoor_work = models.BooleanField()
    air_quality = models.BooleanField()
    waterways_soils = models.BooleanField()
    hazardous_substances = models.BooleanField()
    remotely_isolated_work = models.BooleanField()
    waste = models.BooleanField()
    cultural_heritage = models.BooleanField()
    vehicle_movement = models.BooleanField()

    # high risk construction work
    confined_spaces = models.BooleanField()
    using_explosives = models.BooleanField()
    mobile_plant_movement = models.BooleanField()
    diving_work = models.BooleanField()
    demolition_load_bearing = models.BooleanField()
    artificial_extremes = models.BooleanField()
    asbestos_disturbance = models.BooleanField()
    tilt_up_pre_cast_concrete = models.BooleanField()
    pressurised_gas = models.BooleanField()
    structure_or_buildings = models.BooleanField()
    falling_risk_2m = models.BooleanField()
    working_at_depth = models.BooleanField()
    work_adjacent_road = models.BooleanField()
    work_contaminated = models.BooleanField()
    in_or_near_water = models.BooleanField()

    # ppe
    ppe_1_checkbox = models.BooleanField()
    ppe_2_checkbox = models.BooleanField()
    ppe_3_checkbox = models.BooleanField()
    ppe_4_checkbox = models.BooleanField()
    ppe_5_checkbox = models.BooleanField()
    ppe_6_checkbox = models.BooleanField()
    ppe_7_checkbox = models.BooleanField()
    ppe_8_checkbox = models.BooleanField()
    ppe_9_checkbox = models.BooleanField()
    ppe_10_checkbox = models.BooleanField()
    ppe_11_checkbox = models.BooleanField()
    ppe_12_checkbox = models.BooleanField()

    # permits + hazardous materials
    permits_na = models.BooleanField()
    permits_hotwork = models.BooleanField()
    permits_confinedspace = models.BooleanField()
    permits_localcouncil = models.BooleanField()
    pe_electrical_tools = models.BooleanField()
    pe_handtools = models.BooleanField()
    pe_ladders = models.BooleanField()
    pe_mobile_plant = models.BooleanField()
    hazardous_substances_1 = models.CharField(max_length=100, blank=True)
    hazardous_substances_2 = models.CharField(max_length=100, blank=True)
    hazardous_substances_3 = models.CharField(max_length=100, blank=True)
    hazardous_substances_4 = models.CharField(max_length=100, blank=True)
    hazardous_substances_5 = models.CharField(max_length=100, blank=True)
    hazardous_substances_6 = models.CharField(max_length=100, blank=True)
    hazardous_substances_7 = models.CharField(max_length=100, blank=True)
    hazardous_substances_8 = models.CharField(max_length=100, blank=True)
    hazardous_substances_9 = models.CharField(max_length=100, blank=True)
    hazardous_substances_10 = models.CharField(max_length=100, blank=True)
    hazardous_substances_11 = models.CharField(max_length=100, blank=True)
    hazardous_substances_12 = models.CharField(max_length=100, blank=True)
    sa_audits = models.BooleanField()
    sa_spotchecks = models.BooleanField()
    sa_reportingsystems = models.BooleanField()
    sa_supervisors = models.BooleanField()
    sa_onsitesupervision = models.BooleanField()
    sa_remotesitecomms = models.BooleanField()
    smp_isconstructionproject = models.BooleanField()

    # sign off
    so_workersname_1 = models.CharField(max_length=100, null=True)
    so_jobrole_1 = models.CharField(max_length=100, null=True)
    so_qualification_type_1 = models.CharField(max_length=100, null=True)
    so_qualification_class_1 = models.CharField(max_length=100, null=True)
    so_qualification_number_1 = models.IntegerField(null=True)
    so_signature_1 = models.CharField(max_length=100, null=True)
    so_signature_date_1 = models.DateField(null=True)
    so_workersname_2 = models.CharField(max_length=100, blank=True, null=True)
    so_jobrole_2 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_type_2 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_class_2 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_number_2 = models.IntegerField(blank=True, null=True)
    so_signature_2 = models.CharField(max_length=100, blank=True, null=True)
    so_signature_date_2 = models.DateField(blank=True, null=True)
    so_workersname_3 = models.CharField(max_length=100, blank=True, null=True)
    so_jobrole_3 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_type_3 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_class_3 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_number_3 = models.IntegerField(blank=True, null=True)
    so_signature_3 = models.CharField(max_length=100, blank=True, null=True)
    so_signature_date_3 = models.DateField(blank=True, null=True)
    so_workersname_4 = models.CharField(max_length=100, blank=True, null=True)
    so_jobrole_4 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_type_4 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_class_4 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_number_4 = models.IntegerField(blank=True, null=True)
    so_signature_4 = models.CharField(max_length=100, blank=True, null=True)
    so_signature_date_4 = models.DateField(blank=True, null=True)
    so_workersname_5 = models.CharField(max_length=100, blank=True, null=True)
    so_jobrole_5 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_type_5 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_class_5 = models.CharField(max_length=100, blank=True, null=True)
    so_qualification_number_5 = models.IntegerField(blank=True, null=True)
    so_signature_5 = models.CharField(max_length=100, blank=True, null=True)
    so_signature_date_5 = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.site_number + '-' + self.job_type + self.job_number


class JobTask(models.Model):
    RISK_LEVEL = (
        ('1L', '1L'),
        ('2M', '2M'),
        ('3H', '3H'),
        ('4A', '4A'),
    )
    name = models.CharField(max_length=400, null=True)
    hazards = models.CharField(max_length=400, null=True)
    hazard_risk = models.CharField(max_length=100, null=True, choices=RISK_LEVEL)
    control_measures = models.CharField(max_length=400, null=True)
    control_risk = models.CharField(max_length=100, null=True, choices=RISK_LEVEL)
    responsible_person = models.CharField(max_length=100, blank=True, null=True)
    swms = models.ForeignKey(Swms, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
