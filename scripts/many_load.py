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

        try:
            j = str(row[2])
        except:
            j = None

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lo = float(row[4])
        except:
            lo = None

        try:
            la = float(row[5])
        except:
            la = None

        try:
            a_h = float(row[6])
        except:
            a_h = None



        c, created = Category.objects.get_or_create(name=row[7])
        st, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        s, created = Site.objects.get_or_create(
            name=row[0],description=row[1],justification=j,year=y,
            longitude=lo,latitude=la,area_hectares=a_h,
            category=c, state=st, region=r, iso=i
            )
        # s = Site()
        # s.save()