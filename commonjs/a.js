function calcularIGV(precio) {
  const total = precio / 1.18;
  return total;
}

const IGV = 0.18;

// export calcularIGV
module.exports = {
  calcularIGV,
  IGV: IGV,
};
