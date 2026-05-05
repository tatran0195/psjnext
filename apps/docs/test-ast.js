import remarkMdx from 'remark-mdx';
import remarkParse from 'remark-parse';
import { unified } from 'unified';

const md = `
## Inputs

<!-- @type:Boolean @required @since:5.0.1 @removed:5.2.0 -->
### \`bIsMergePart\`

- The is merge part.
`;

const ast = unified().use(remarkParse).use(remarkMdx).parse(md);

console.log(JSON.stringify(ast, null, 2));
