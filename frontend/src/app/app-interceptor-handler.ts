import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';
import { finalize } from 'rxjs/operators';
import { CarregandoService } from './services/carregamento/carregamento.service';

@Injectable()
export class ApplicationInterceptorHandler implements HttpInterceptor  {

  requisicoesAtivas: number = 0;

  constructor(private servico: CarregandoService) {  }

  intercept(requisicao: HttpRequest<any>, proximo: HttpHandler): Observable<HttpEvent<any>> {

    if (this.requisicoesAtivas === 0) {
      this.servico.iniciarCarregamento();
    }

    this.requisicoesAtivas++;

    return proximo.handle(requisicao).pipe(
      finalize(() => {
        this.requisicoesAtivas--;
        if (this.requisicoesAtivas === 0) {
          this.servico.pararCarregamento();
        }
      })
    );
  }
}
