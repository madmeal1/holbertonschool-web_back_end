const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", () => {
  describe("SUM", () => {
    it("rounds and adds two numbers", () => {
      assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
    });

    it("works with decimals below .5", () => {
      assert.strictEqual(calculateNumber("SUM", 1.2, 3.4), 4);
    });
  });

  describe("SUBTRACT", () => {
    it("rounds and subtracts b from a", () => {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
    });

    it("works with decimals below .5", () => {
      assert.strictEqual(calculateNumber("SUBTRACT", 5.4, 2.4), 3);
    });
  });

  describe("DIVIDE", () => {
    it("rounds and divides a by b", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
    });

    it("returns Error when rounded b is 0", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
    });

    it("returns Error when b rounds down to 0", () => {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0.2), "Error");
    });
  });
});
