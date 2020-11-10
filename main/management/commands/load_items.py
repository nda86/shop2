import csv
import logging

from django.core.management.base import BaseCommand
from main.models import Item


log = logging.getLogger("command_debug_log")


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="Путь к файлу с товарами")
        parser.add_argument("--clear", action="store_true", help="Очищать таблицу перед добавлением")

    def handle(self, *args, **options):
        if options["clear"]:
            Item.objects.all().delete()

        with open(options["path"], "r") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                articul = "ПТ" + row[0]
                title = row[1]
                price_post = int(row[2])
                price_zakup = 0.9 * price_post
                price_rozn = 1.2 * price_post if price_post < 1000 else 1.1 * price_post

                item = Item()
                item.articul = articul
                item.title = title
                item.price_zakup = price_zakup
                item.price_rozn = price_rozn
                try:
                    item.save()
                    log.debug(f"Создан товар {item}")
                except Exception as e:
                    log.error(f"{e} --- {row}")
