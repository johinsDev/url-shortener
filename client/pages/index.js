import * as React from "react";
import Link from "next/link";
import { CSSTransition } from "react-transition-group";
import fetcher from "../libs/fetch";

const id = 1;

export default function IndexPage() {
  const [url, setUrl] = React.useState("");

  const [shortenedUrl, setShortenedUrl] = React.useState();

  async function onSubmit(e) {
    e.preventDefault();

    try {
      const data = await fetcher("http://localhost:5000/api/v1/links", {
        body: JSON.stringify({ url }),
        method: "POST",
      });

      setShortenedUrl(data);
    } catch (error) {
      console.log("error", error);
    }
  }

  return (
    <div className="w-full">
      <form action="#" noValidate className="w-full mb-16" onSubmit={onSubmit}>
        <input
          type="url"
          placeholder="Let`s get you a short URL"
          className="text-xl p-5 w-full outline-none border-0 rounded-sm"
          onChange={(e) => setUrl(e.target.value)}
        />
      </form>
      <CSSTransition
        in={!!shortenedUrl}
        timeout={200}
        classNames="shortened"
        unmountOnExit
      >
        <div className="w-full text-center flex justify-between items-center mx-auto md:w-4/5">
          <div className="text-white text-2xl mb-8">
            <div className="opacity-50 mb-2 flex flex-wrap justify-center">
              <span className="inline-block max-w-xs truncate mr-2">
                {shortenedUrl?.original_url}
              </span>
              is now
            </div>

            <a
              target="_blank"
              className="mb-8 text-white block underline cursor-pointer"
              href={shortenedUrl?.shortened_url}
            >
              {shortenedUrl?.shortened_url}
            </a>

            <Link href={`/stats/[id]`} as={`/stats/${shortenedUrl?.code}`}>
              <a className="text-white block underline cursor-pointer">
                Get stats
              </a>
            </Link>
          </div>

          <button
            className="button button-yellow"
            onClick={onSubmit}
            disabled={!url}
          >
            Copy to clipboard
          </button>
        </div>
      </CSSTransition>
      <div className="text-white text-center font-medium text-lg mt-12">
        Hit return when you`re done
      </div>
    </div>
  );
}
