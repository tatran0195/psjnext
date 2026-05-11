import remarkParse from 'remark-parse';
import { unified } from 'unified';

const md = `
<details>
    <summary>List of newly added command</summary>

    - \`JPT.ShowMultiMappingData\`
    - \`JPT.OtherCommand\`

</details>
`;

const processor = unified().use(remarkParse);
const ast = processor.parse(md);

console.log(JSON.stringify(ast, null, 2));
