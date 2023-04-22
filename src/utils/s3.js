import S3 from "aws-sdk/clients/s3.js";
import fs from "fs";

export const subirImagenes = (ubicacion) => {
  const s3 = new S3({
    region: process.env.AWS_BUCKET_REGION,
    credentials: {
      accessKeyId: process.env.AWS_ACCESS_KEY,
      secretAccessKey: process.env.AWS_SECRET_KEY,
    },
  });

  const fileStream = fs.createReadStream("./piscina.jpg");

  const archivoSubido = s3
    .upload({
      Bucket: process.env.AWS_BUCKET_NAME,
      Body: fileStream,
      Key: "piscina.jpg", // nombre del archivo
    })
    .promise();

  return archivoSubido;
};
