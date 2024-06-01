import { pgTableCreator } from 'drizzle-orm/pg-core';
import { snakeCase } from 'lodash';

export const createTable = pgTableCreator((name) => `na_${snakeCase(name)}`);
