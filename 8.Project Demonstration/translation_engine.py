# ==============================================================================
# AgriGuard AI - Indic Language Translation Engine
# Epic 4: Ensemble AI & Synthesis Architecture
# Story: Indic Language Engine for 6-Language Translation with Agricultural Tone
# ==============================================================================

import logging
from typing import Dict, Any, List, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Supported 6 Indic Languages Mapping
INDIC_LANGUAGES = {
    "hi": "Hindi",
    "bn": "Bengali",
    "te": "Telugu",
    "ta": "Tamil",
    "mr": "Marathi",
    "gu": "Gujarati"
}


class IndicTranslationEngine:
    """
    Translates AgriGuard AI crop advisories into 6 major Indic languages:
    Hindi (hi), Bengali (bn), Telugu (te), Tamil (ta), Marathi (mr), Gujarati (gu).
    """

    def __init__(self):
        self.supported_langs = INDIC_LANGUAGES

    def translate_advisory(
        self,
        text: str,
        target_lang: str,
        source_lang: str = "en"
    ) -> Dict[str, Any]:
        """
        Translates structured agricultural text to target Indic language.
        """
        lang_code = target_lang.lower().strip()

        if lang_code not in self.supported_langs:
            logging.warning(f"Language code '{target_lang}' unsupported. Returning original English text.")
            return {
                "status": "UNSUPPORTED_LANGUAGE",
                "translated_text": text,
                "target_language": target_lang,
                "source_language": source_lang
            }

        if lang_code == source_lang:
            return {
                "status": "NO_TRANSLATION_REQUIRED",
                "translated_text": text,
                "target_language": target_lang,
                "source_language": source_lang
            }

        try:
            from deep_translator import GoogleTranslator
            translator = GoogleTranslator(source=source_lang, target=lang_code)
            translated_result = translator.translate(text)

            return {
                "status": "SUCCESS",
                "translated_text": translated_result,
                "target_language": self.supported_langs[lang_code],
                "target_code": lang_code,
                "source_language": source_lang
            }

        except Exception as e:
            logging.error(f"Translation engine failed for language '{lang_code}': {e}")
            return self._fallback_translation(text, lang_code, source_lang, str(e))

    def _fallback_translation(
        self,
        text: str,
        target_lang: str,
        source_lang: str,
        error_msg: str
    ) -> Dict[str, Any]:
        """Generates fallback response if offline or service fails."""
        lang_name = self.supported_langs.get(target_lang, target_lang)
        return {
            "status": "FALLBACK",
            "translated_text": f"[{lang_name.upper()} ADVISORY]: {text}",
            "target_language": lang_name,
            "target_code": target_lang,
            "source_language": source_lang,
            "error_detail": error_msg
        }

    def translate_all_6_languages(self, text: str) -> Dict[str, str]:
        """
        Translates an advisory into all 6 supported Indic languages simultaneously.
        """
        multilingual_advisories = {}
        for code, lang_name in self.supported_langs.items():
            res = self.translate_advisory(text, target_lang=code)
            multilingual_advisories[lang_name] = res["translated_text"]
        return multilingual_advisories


# Standalone execution test
if __name__ == "__main__":
    import json
    
    engine = IndicTranslationEngine()
    sample_text = (
        "Apply 40 kg/ha Nitrogen balance before sowing. "
        "Moderate drought risk detected; implement drip irrigation cycle."
    )

    print("Testing 6-Language Indic Translation Engine:\n")
    results = engine.translate_all_6_languages(sample_text)
    print(json.dumps(results, indent=2, ensure_ascii=False))