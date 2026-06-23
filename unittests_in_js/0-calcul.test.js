const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('returns the sum of two rounded integers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('rounds b up when decimal is >= .5', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('rounds both numbers correctly', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('rounds a up when decimal is .5', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('rounds decimals below .5 down', () => {
    assert.strictEqual(calculateNumber(1.4, 4.4), 5);
  });

  it('handles negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.5, 3.7), 3);
  });
});
