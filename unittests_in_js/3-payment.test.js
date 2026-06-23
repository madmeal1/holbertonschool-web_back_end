const sinon = require("sinon");
const assert = require("assert");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi", () => {
  it("calls Utils.calculateNumber with SUM, totalAmount, and totalShipping", () => {
    const spy = sinon.spy(Utils, "calculateNumber");

    sendPaymentRequestToApi(100, 20);

    assert(spy.calledOnce);
    assert(spy.calledWith("SUM", 100, 20));

    spy.restore();
  });
});
