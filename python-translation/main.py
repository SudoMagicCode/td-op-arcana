import googletrans
import json
import os
import asyncio

translator = googletrans.Translator()
target_languages = ['es', 'fr', 'de', 'zh-cn']
root_dir: str = "../TouchDesigner/tox/examples"
op_dirs: list[str] = [
    "COMP", "CHOP", "TOP", "SOP", "POP", "MAT", "DAT"
]


async def find_md_files() -> list[str]:
    md_files = []
    for each_dir in op_dirs:
        search_dir: str = f"{root_dir}/{each_dir}/readme"

        for each_file in os.listdir(search_dir):
            full_path: str = f"{search_dir}/{each_file}"
            if os.path.isfile(full_path):
                root, ext = os.path.splitext(full_path)

                if ext == '.md':
                    print(f"    processing md file {full_path}")
                    await create_translations(
                        sourceFile=full_path, outputFile=f'{root}_translation.py')

    return md_files


async def create_translations(sourceFile: str, outputFile: str) -> None:
    with open(outputFile, 'w+', encoding='utf-8') as translation_file:
        print(f"    generating translation")
        translations: dict = await generate_translations(sourceFile)
        output_content: str = f"content = {json.dumps(translations, indent=4, ensure_ascii=False)}"
        translation_file.write(output_content)


async def generate_translations(sourceFile: str) -> dict:
    translation_dict = {}

    with open(sourceFile, 'r') as source:
        data: str = source.read()
        en: str = data
        print("        translating to en")
        translation_dict['en'] = en
        for each in target_languages:
            print(f"        translating to {each}")
            translation = await translator.translate(data, each)
            translation_dict[each] = translation.text

    return translation_dict


async def main():
    print("Starting translation process")
    await find_md_files()


if __name__ == '__main__':
    asyncio.run(main())
