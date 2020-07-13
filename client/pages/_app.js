import "../styles/index.css";

function MyApp({ Component, pageProps }) {
  return (
    <main className="container mx-auto p-6 flex flex-col justify-center items-center min-h-full">
      <Component {...pageProps} />
    </main>
  );
}

export default MyApp;
