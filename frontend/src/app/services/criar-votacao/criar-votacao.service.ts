import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CriarVotacaoService {

  private urlApi = `${environment.url}`;

  constructor(private http: HttpClient) { }


}
