function openMerchantModal() {
  document.getElementById('merchantAddProductModal').classList.add('active');
}

function closeMerchantModal() {
  document.getElementById('merchantAddProductModal').classList.remove('active');
}

document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('merchantAddProductModal');
  if (!modal) return;

  modal.addEventListener('click', function (e) {
    if (e.target === modal) {
      closeMerchantModal();
    }
  });
});