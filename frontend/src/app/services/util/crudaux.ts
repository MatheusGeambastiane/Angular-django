import { Const } from "src/app/ultil/const";
// Util
import { HttpClient } from "@angular/common/http"

export class Crudaux {
    constructor(public http: HttpClient, public constant: Const, public entity: string){}

    async search(fields: any) {
        if (fields){
            return await this.http.get<any[]>(this.constant.BackUrlBase + this.entity
                , fields).toPromise();
    
                
                
            }
        else{    
            return await this.http.get<any[]>(this.constant.BackUrlBase + 
                this.entity).toPromise();
            }
    
    }

    async add(fields: any) {
        return await this.http.post<any[]>(this.constant.BackUrlBase + this.entity
            , fields).toPromise();

    }
    async update(fields: any) {
        return await this.http.put<any[]>(this.constant.BackUrlBase + this.entity
            , fields).toPromise();

    }
    async delete(fields: any) {
        return await this.http.delete<any[]>(this.const.BackUrlBase + this.entity
            , fields).toPromise();

    }
}
