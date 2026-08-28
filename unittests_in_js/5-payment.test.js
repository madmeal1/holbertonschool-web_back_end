const sinon = require("sinon");
const assert = require("assert");
const sendPaymentRequestToApi = require("./5-payment");

describe("sendPaymentRequestToApi", () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, "log");
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it("logs The total is: 120 when called with 100 and 20", () => {
    sendPaymentRequestToApi(100, 20);

    assert(consoleSpy.calledOnce);
    assert(consoleSpy.calledWith("The total is: 120"));
  });

  it("logs The total is: 20 when called with 10 and 10", () => {
    sendPaymentRequestToApi(10, 10);

    assert(consoleSpy.calledOnce);
    assert(consoleSpy.calledWith("The total is: 20"));
  });
});
