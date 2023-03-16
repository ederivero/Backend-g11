const getSuspense = (promise) => {
  let status = "pending";
  let result;

  let suspender = promise.then(
    (response) => {
      status = "success";
      result = response;
    },
    (error) => {
      status = "error";
      result = error;
    }
  );

  const read = () => {
    switch (status) {
      case "pending":
        throw suspender;
      case "error":
        throw result;
      default:
        return result;
    }
  };

  return { read };
};

export const axios = (url) => {
  const promise = fetch(url)
    .then((response) => response.json())
    .then((data) => data)

  return getSuspense(promise);
};
