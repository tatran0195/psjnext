import { create } from '@orama/orama';
import { createTokenizer } from '@orama/tokenizers/japanese';
import { stopwords as japaneseStopwords } from '@orama/stopwords/japanese';

export function initOrama(locale?: string) {
    const isJapanese = locale === 'ja';

    return create({
        schema: {
            id: 'string',
            title: 'string',
            description: 'string',
            content: 'string',
            url: 'string',
            tag: 'string',
        },
        language: isJapanese ? undefined : 'english',
        components: {
            tokenizer: isJapanese
                ? createTokenizer({
                      language: 'japanese',
                      stopWords: japaneseStopwords,
                  })
                : undefined,
        },
    });
}
