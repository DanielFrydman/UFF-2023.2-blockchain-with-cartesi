import { AmbienteService } from "./ambiente.service";

export const AmbienteServiceFactory = () => {

  const ambiente = new AmbienteService();

  const navegadorCliente = window || {};
  // @ts-ignore
  const navegadorClienteAmbiente = navegadorCliente['__ambiente'] || {};

  for (const chave in navegadorClienteAmbiente) {
    if (navegadorClienteAmbiente.hasOwnProperty(chave)) {
      // @ts-ignore
      ambiente[chave] = window['__ambiente'][chave];
    }
  }

  return ambiente;
};

export const AmbienteServiceProvider = {
  provide: AmbienteService,
  useFactory: AmbienteServiceFactory,
  deps: [],
};
