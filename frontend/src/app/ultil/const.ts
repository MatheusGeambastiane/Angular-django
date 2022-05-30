import { Injectable } from "@angular/core";
import { environment } from "src/environments/environment";

@Injectable()
export class Const {

    readonly BackUrlBase = environment.ApiUrl;
}
