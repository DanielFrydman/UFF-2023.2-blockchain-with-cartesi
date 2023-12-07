import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CarregandoService {

  carregando$: Subject<boolean> = new Subject();

  constructor() { }

  iniciarCarregamento() {
    this.carregando$.next(true);
  }

  pararCarregamento() {
    this.carregando$.next(false);
  }
}
