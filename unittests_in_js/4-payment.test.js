const sinon = require("sinon");
const assert = require("assert");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");

describe("sendPaymentRequestToApi", () => {
  it("calls Utils.calculateNumber with SUM, totalAmount, and totalShipping, and logs the correct total", () => {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);
    const spy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    assert(stub.calledOnce);
    assert(stub.calledWith("SUM", 100, 20));
    assert(spy.calledWith("The total is: 10"));

    stub.restore();
    spy.restore();
  });
});
