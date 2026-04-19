/*
 * annotatedMatMul.test.ts
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 * Author: Eric Traut
 *
 * Unit tests for pyright type evaluator with MatMul Annotated syntax.
 */

import { ConfigOptions } from '../common/configOptions';
import { pythonVersion3_16 } from '../common/pythonVersion';
import { Uri } from '../common/uri/uri';
import * as TestUtils from './testUtils';

test('AnnotatedMatMul1', () => {
    const configOptions = new ConfigOptions(Uri.empty());
    configOptions.defaultPythonVersion = pythonVersion3_16;

    const analysisResults = TestUtils.typeAnalyzeSampleFiles(['annotatedMatMul1.py'], configOptions);

    TestUtils.validateResults(analysisResults, 0);
});
