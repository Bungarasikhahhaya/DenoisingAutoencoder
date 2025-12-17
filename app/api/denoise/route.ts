import { NextRequest, NextResponse } from "next/server";

export const runtime = "nodejs"; // pastikan running di server

export async function POST(req: NextRequest) {
  try {
    const formData = await req.formData();
    const file = formData.get("image");

    if (!file || !(file instanceof Blob)) {
      return NextResponse.json({ error: "no image" }, { status: 400 });
    }

    const backendForm = new FormData();
    backendForm.append("image", file, "upload.png");

    const res = await fetch("http://localhost:5000/api/denoise", {
      method: "POST",
      body: backendForm,
    });

    const text = await res.text(); // baca sebagai teks dulu

    // Coba parse sebagai JSON; kalau gagal, kirim teks mentah
    try {
      const data = JSON.parse(text);
      return NextResponse.json(data, { status: res.status });
    } catch {
      console.error("Response dari Flask bukan JSON:", text);
      return NextResponse.json(
        { error: "proxy error", detail: text },
        { status: res.status || 500 }
      );
    }
  } catch (err: any) {
    console.error("Error proxy ke Flask:", err);
    return NextResponse.json(
      { error: "proxy error", detail: String(err) },
      { status: 500 }
    );
  }
}
