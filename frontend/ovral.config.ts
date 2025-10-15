export default {
    skoga: {
      // uses the file our Django command already writes
      input: './openapi.json',
      output: {
        target: 'src/api/skoga.gen.ts',
        client: 'react-query',   // generates hooks + axios client
        httpClient: 'axios',
        mock: false,
        prettier: true,
      },
      hooks: true,
    },
  };
  