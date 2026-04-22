import { createJCall } from 'jcall';
import path from 'node:path';

export const jcall = createJCall({
    input: path.resolve('./content/api/sdk.jcall.yaml'),
});
