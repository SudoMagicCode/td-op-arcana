import googletrans
import json
import os
import asyncio

translator = googletrans.Translator()
target_languages = ['es']
root_dir: str = "../TouchDesigner/tox/examples"
op_dirs: list[str] = [
    "COMP", "CHOP", "TOP", "SOP", "POP", "MAT", "DAT"
]


def find_md_files() -> list[str]:
    md_files = []
    for each_dir in op_dirs:
        search_dir: str = f"{root_dir}/{each_dir}/readme"

        for each_file in os.listdir(search_dir):
            full_path: str = f"{search_dir}/{each_file}"
            if os.path.isfile(full_path):
                root, ext = os.path.splitext(full_path)

                if ext == '.md':
                    print(f"found a md file {full_path}")
                    create_translations(
                        sourceFile=full_path, outputFile=f'{root}_translation.py')

    return md_files


def create_translations(sourceFile: str, outputFile: str) -> None:
    with open(outputFile, 'w+') as translation_file:
        print("    generating translation")
        translations: dict = generate_translations(sourceFile)
        output_content: str = f"content = {json.dumps(translations, indent=4)}"
        translation_file.write(output_content)


async def generate_translations(sourceFile: str) -> dict:
    translation_dict = {}

    with open(sourceFile, 'r') as source:
        data: str = source.read()
        en: str = data
        translation_dict['en'] = en
        for each in target_languages:
            translation = translator.translate(data, each)
            await translation
            translation_dict[each] = translation

    return translation_dict


def main():
    md_files = find_md_files()


if __name__ == '__main__':
    main()
