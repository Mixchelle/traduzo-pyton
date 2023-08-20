# src/controllers/translate_controller.py
from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel

translate_controller = Blueprint("translate_controller", __name__)

@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        translated_text = GoogleTranslator(
            source=translate_from,
            target=translate_to).translate(text_to_translate)

        history_data = {
            "original_text": text_to_translate,
            "translated_text": translated_text,
            "source_language": translate_from,
            "target_language": translate_to
        }

        HistoryModel(history_data).save()  

        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated_text
        )

    text_to_translate = "O que deseja traduzir"
    translate_from = "pt"
    translate_to = "en"
    translated = "Tradução"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )

@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    if request.method != "POST":
        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            translated="Tradução")
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(
        source=translate_from,
        target=translate_to
        ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=request.form["translate-to"],
        translate_to=request.form["translate-from"],
        translated=translated,
    )
