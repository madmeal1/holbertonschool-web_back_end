const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');


describe('calculateNumber', () => {
  describe('SUM', () => {
    it('rounds and adds two numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('works with decimals below .5', () => {
      expect(calculateNumber('SUM', 1.2, 3.4)).to.equal(4);
    });
  });

  describe('SUBTRACT', () => {
    it('rounds and subtracts b from a', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('works with decimals below .5', () => {
      expect(calculateNumber('SUBTRACT', 5.4, 2.4)).to.equal(3);
    });
  });

  describe('DIVIDE', () => {
    it('rounds and divides a by b', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('returns Error when rounded b is 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('returns Error when b rounds down to 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
    });
  });
});
