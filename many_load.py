import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Region, Iso, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        si_n, created = Site.objects.get_or_create(name=row[0])
        si_d, created = Site.objects.get_or_create(description=row[1])
        si_j, created = Site.objects.get_or_create(justification=row[2])
        si_y, created = Site.objects.get_or_create(year=row[3])
        si_lo, created = Site.objects.get_or_create(longitude=row[4])
        si_la, created = Site.objects.get_or_create(latitude=row[5])
        si_a, created = Site.objects.get_or_create(area_hectares=row[6])
        c, created = Category.objects.get_or_create(name=row[7])
        st, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        # r = Membership.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Membership(role=r, person=p, course=c)
        # m.save()