import "../styles/globals.css";
import type { AppProps } from "next/app";
import JSX from "next";

export default function App({ Component, pageProps }: AppProps): JSX.Element {
  return <Component {...pageProps} />;
}
