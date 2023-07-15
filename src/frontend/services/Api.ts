import axios, { AxiosInstance, AxiosResponse } from "axios";

class Api<T, K> {
  private api: AxiosInstance;
  constructor(baseURL: string) {
    this.api = axios.create({
      baseURL,
    });
  }

  public get(path: string, params: any): Promise<AxiosResponse<T>> {
    return this.api.get(path, params);
  }
  public post(path: string, data: T): Promise<AxiosResponse<K>> {
    return this.api.post(path, data);
  }
  public put(path: string, data: T): Promise<AxiosResponse<T>> {
    return this.api.put(path, data);
  }
  public patch(path: string, data: T): Promise<T> {
    return this.api.patch(path, data);
  }
  public delete(path: string): Promise<T> {
    return this.api.delete(path);
  }
}

export default Api;
