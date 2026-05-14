import remarkDirective from 'remark-directive'
import remarkFrontmatter from 'remark-frontmatter'
import remarkGfm from 'remark-gfm'
import remarkPresetLintConsistent from 'remark-preset-lint-consistent'
import remarkPresetLintRecommended from 'remark-preset-lint-recommended'

const config = {
  plugins: [
    remarkFrontmatter,
    remarkGfm,
    remarkDirective,
    remarkPresetLintConsistent,
    remarkPresetLintRecommended,

    // ── Rule overrides to prevent mangling ──────────────────────────────
    ['remark-lint-emphasis-marker', '_'],          // keep _ not *
    ['remark-lint-strong-marker', '*'],            // keep * for bold
    ['remark-lint-no-undefined-references', false],// stop \| escaping
    ['remark-lint-maximum-line-length', false],    // stop line-wrap rewrites
  ],

  // ── remark-stringify settings ────────────────────────────────────────
  settings: {
    emphasis: '_',          // serialize _ not *
    strong: '*',            // serialize * not _
    bullet: '-',            // keep - not *
    listItemIndent: 'one',  // single space after list marker
    fences: true,           // always use ``` not indented code blocks
    incrementListMarker: false,
  },
}

export default config