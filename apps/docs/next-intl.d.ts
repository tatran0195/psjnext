import en from './locales/en.json';

declare module 'next-intl' {
    interface AppConfig {
        // Locale union
        Locale: 'en' | 'ja';
        // Message shape — derived from en.json (source of truth)
        Messages: typeof en;
    }
}
