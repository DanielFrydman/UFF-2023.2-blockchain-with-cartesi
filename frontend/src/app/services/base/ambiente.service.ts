import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AmbienteService {

  public enableDebug = true;

  public numeroRequisicao = 0;

  constructor() { }
}
