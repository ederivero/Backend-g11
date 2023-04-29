import S3 from "aws-sdk/clients/s3.js";
import fs from "fs";

export const subirImagenes = (archivo) => {
  const s3 = new S3({
    region: process.env.AWS_BUCKET_REGION,
    credentials: {
      accessKeyId: process.env.AWS_ACCESS_KEY,
      secretAccessKey: process.env.AWS_SECRET_KEY,
    },
  });

  const fileStream = fs.createReadStream(`${archivo.path}`);

  const archivoSubido = s3
    .upload({
      Bucket: process.env.AWS_BUCKET_NAME,
      Body: fileStream,
      Key: archivo.filename, // nombre del archivo
    })
    .promise();

  return archivoSubido;
};

export const devolverUrlFirmada = (archivo) => {
  const s3 = new S3({
    region: process.env.AWS_BUCKET_REGION,
    credentials: {
      accessKeyId: process.env.AWS_ACCESS_KEY,
      secretAccessKey: process.env.AWS_SECRET_KEY,
    },
  });
  // Creo una URL firmada para que pueda acceder al archivo dentro de un determinado tiempo
  const url = s3.getSignedUrl("getObject", {
    Bucket: process.env.AWS_BUCKET_NAME,
    Key: archivo,
    Expires: 30, // Numero expresado en segundos
  });

  return url;
};

export const eliminarArchivo = (archivo) => {
  const s3 = new S3({
    region: process.env.AWS_BUCKET_REGION,
    credentials: {
      accessKeyId: process.env.AWS_ACCESS_KEY,
      secretAccessKey: process.env.AWS_SECRET_KEY,
    },
  });

  s3.deleteObject(
    {
      Bucket: process.env.AWS_BUCKET_NAME,
      Key: archivo,
    },
    (err, data) => {
      if (err) {
        throw new Error(err);
      }
      if (data) {
        console.log(data);
      }
    }
  );
};
