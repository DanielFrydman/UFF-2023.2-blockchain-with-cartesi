import { Injectable } from '@angular/core';
import { HttpHeaders, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export abstract class BaseService {


  private obterTokenUsuario() {
    return sessionStorage.getItem('app.token');
  }

  protected SalvarLogin(login: string) {
    sessionStorage.setItem('app.usuario', login);
  }

  protected SalvarToken(token: string) {
    sessionStorage.setItem('app.token', token);
  }

  protected SalvarPermissoes(permissoes: []) {
    let permisao: string = "";

    permissoes.forEach(function (p) {
      permisao += ''.concat(', ', p);
    });

    sessionStorage.setItem('app.permissoes', permisao);
  }

  protected ObterCodigoUsuario() {
    return sessionStorage.getItem('app.usuario');
  }

  protected ObterPermissoes() {
      return sessionStorage.getItem('app.permissoes');
  }

  protected ObterAuthHeader() {
    return {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${this.obterTokenUsuario()}`
      })
    };
  }

  protected ObterAutenticacaoComParametrosNoHeader(parametros: HttpParams) {
    return {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${this.obterTokenUsuario()}`,
      }),
      params: parametros

    };
  }

  protected ObterHeader() {
    return new HttpHeaders({
      'Authorization': `Bearer ${this.obterTokenUsuario()}`
      })
  }

  montarDownloadArquivo(dados: any, tipo: string, nomeRelatorio: string) {
    let blob = new Blob([dados], { type: tipo });
    let url = window.URL.createObjectURL(blob);
    let element = document.createElement('a');
    element.href = url;
    element.download = nomeRelatorio;
    document.body.appendChild(element);
    element.click();
  }
}
