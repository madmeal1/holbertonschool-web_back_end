const assert = require("assert");
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("getPaymentTokenFromAPI", () => {
  it("returns a resolved promise with the correct response when success is true", (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      assert.deepStrictEqual(response, {
        data: "Successful response from the API",
      });
      done();
    });
  });
});
